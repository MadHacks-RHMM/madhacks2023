package com.example.allaround;

import android.content.Intent;
import android.os.Bundle;
import android.view.Menu;
import android.view.MenuInflater;
import android.view.MenuItem;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

import androidx.activity.result.ActivityResultLauncher;
import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;

import com.example.allaround.network.LinkTokenRequester;
import com.plaid.link.OpenPlaidLink;
import com.plaid.link.configuration.LinkTokenConfiguration;
import com.plaid.link.result.LinkExit;
import com.plaid.link.result.LinkSuccess;

/**
 * Implemented with reference from https://github.com/plaid/plaid-link-android.git
 * including res/value/strings.xml, network/LinkSampleApi.kt, network/LinkTokenRequester
 */
public class SignupActivity extends AppCompatActivity {


    private TextView result;
    private TextView tokenResult;

    private ActivityResultLauncher<LinkTokenConfiguration> linkAccountToPlaid = registerForActivityResult(
            new OpenPlaidLink(),
            result -> {
                if (result instanceof LinkSuccess) {
                    showSuccess((LinkSuccess) result);
                } else {
                    showFailure((LinkExit) result);
                }
            });
    private void showSuccess(LinkSuccess success) {
        tokenResult.setText(getString(R.string.public_token_result, success.getPublicToken()));
        result.setText(getString(R.string.content_success));
    }

    private void showFailure(LinkExit exit) {
        tokenResult.setText("");
        if (exit.getError() != null) {
            result.setText(getString(
                    R.string.content_exit,
                    exit.getError().getDisplayMessage(),
                    exit.getError().getErrorCode()));
        } else {
            result.setText(getString(
                    R.string.content_cancel,
                    exit.getMetadata().getStatus() != null ? exit.getMetadata().getStatus().getJsonValue() : "unknown"));
        }
    }


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_signup);


        Button SignupStartBtn = (Button)findViewById(R.id.SignupStartBtn);
        EditText EditMonthly = (EditText)findViewById(R.id.MonthlyGoal);



        SignupStartBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                String monthlygoal = EditMonthly.getText().toString();
                Client.getInstance().setMontlyGoal(Integer.parseInt("100"));



                Intent intent = new Intent(SignupActivity.this,HomeActivity.class);
                openLink();
                startActivity(intent);











            }
        });

    }
    private void openLink() {
        LinkTokenRequester.INSTANCE.getToken()
                .subscribe(this::onLinkTokenSuccess, this::onLinkTokenError);
    }

    private void onLinkTokenSuccess(String token) {
        LinkTokenConfiguration configuration = new LinkTokenConfiguration.Builder()
                .token(token)
                .build();
        linkAccountToPlaid.launch(configuration);
    }

    private void onLinkTokenError(Throwable error) {
        if (error instanceof java.net.ConnectException) {
            Toast.makeText(
                    this,
                    "",
                    Toast.LENGTH_LONG).show();
            return;
        }
        Toast.makeText(this, error.getMessage(), Toast.LENGTH_SHORT).show();
    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        MenuInflater inflater = getMenuInflater();
        inflater.inflate(R.menu.menu_java, menu);
        return true;
    }

    @SuppressWarnings("SwitchStatementWithTooFewBranches")
    @Override
    public boolean onOptionsItemSelected(@NonNull MenuItem item) {
        switch (item.getItemId()) {
            case R.id.show_kotlin:
                Intent intent = new Intent(this, SignupActivity.class);
                intent.setFlags(Intent.FLAG_ACTIVITY_NEW_TASK | Intent.FLAG_ACTIVITY_CLEAR_TASK);
                startActivity(intent);
                return true;
            default:
                return super.onOptionsItemSelected(item);
        }
    }
}




