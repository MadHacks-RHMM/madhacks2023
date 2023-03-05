package com.example.allaround;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;

import com.google.android.gms.auth.api.signin.GoogleSignIn;
import com.google.android.gms.auth.api.signin.GoogleSignInAccount;
import com.google.android.gms.auth.api.signin.GoogleSignInClient;
import com.google.android.gms.auth.api.signin.GoogleSignInOptions;
import com.google.android.gms.common.api.ApiException;
import com.google.android.gms.tasks.Task;

import retrofit2.Retrofit;
import retrofit2.converter.gson.GsonConverterFactory;

public class MainActivity extends AppCompatActivity {

    private Retrofit retrofit;
    private RetrofitInterface retrofitInterface;
    private String BASE_URL = "http://10.0.2.2:8000/";

    GoogleSignInOptions gso;
    GoogleSignInClient gsc;
    Button googleBtn;



    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);



        gso = new GoogleSignInOptions.Builder(GoogleSignInOptions.DEFAULT_SIGN_IN).requestEmail().build();
        gsc = GoogleSignIn.getClient(this,gso);

//        GoogleSignInAccount acct = GoogleSignIn.getLastSignedInAccount(this);
//        if(acct!=null){
//            Client.getInstance().setName(acct.getDisplayName());
//            Client.getInstance().setEmail(acct.getEmail());
//            Client.getInstance().setMontlyGoal(100);
//
//            navigateToSecondActivity();
//        }
        googleBtn = findViewById(R.id.googleBtn);

        googleBtn.setOnClickListener(new View.OnClickListener() {



            @Override
            public void onClick(View v) {
                signIn();
            }
        });
    }




    @Override
    protected void onActivityResult(int requestCode, int resultCode,Intent data) {
        retrofit = new Retrofit.Builder()
                .baseUrl(BASE_URL)
                .addConverterFactory(GsonConverterFactory.create())
                .build();

        retrofitInterface = retrofit.create(RetrofitInterface.class);
        super.onActivityResult(requestCode, resultCode, data);
        if(requestCode == 1000){
            Task<GoogleSignInAccount> task = GoogleSignIn.getSignedInAccountFromIntent(data);

            try {
                GoogleSignInAccount acct = task.getResult(ApiException.class);
                if (acct != null) {
                    Client.getInstance().setName(acct.getDisplayName());
                    Client.getInstance().setEmail(acct.getEmail());
                    Client.getInstance().setMontlyGoal(100);
//
//                    HashMap<String, String> map = new HashMap<>();
//                    map.put("name", acct.getDisplayName());
//                    map.put("email", acct.getEmail());
//                    Call<Boolean> call = retrofitInterface.executeLogin(map);
//
//                    call.enqueue(new Callback<Boolean>() {
//                        @Override
//                        public void onResponse(@NonNull Call<Boolean> call, @NonNull Response<Boolean> response) {
//                            if(response.code() == 200){
//                                if(response.body()){
//                                    startActivity(new Intent(MainActivity.this, HomeActivity.class));
//
//                                }
//                                else{
//                                    startActivity(new Intent(MainActivity.this, SignupActivity.class));
//                                }
//                            }
//                            else{
//                                Toast.makeText(MainActivity.this, "Wrong Credentials CODE # " + response.code(),
//                                        Toast.LENGTH_LONG).show();
//                            }
//                        }
//
//
//                        @Override
//                        public void onFailure(@NonNull Call<Boolean> call, @NonNull Throwable t) {
//                            Toast.makeText(MainActivity.this, t.getMessage(),
//                                    Toast.LENGTH_LONG).show();
//                        }
//
//
//                    });



















                }



                navigateToSecondActivity();
            } catch (ApiException e) {
                Toast.makeText(getApplicationContext(), "Wrong Credential", Toast.LENGTH_SHORT).show();
            }
        }

    }
    void navigateToSecondActivity(){

        Intent intent = new Intent(MainActivity.this,SignupActivity.class);
        startActivity(intent);
    }
    void signIn(){
        Intent signInIntent = gsc.getSignInIntent();
        startActivityForResult(signInIntent,1000);
    }
}