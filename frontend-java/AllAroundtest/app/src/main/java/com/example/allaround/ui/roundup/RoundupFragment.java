package com.example.allaround.ui.roundup;

import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Switch;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.fragment.app.Fragment;
import androidx.lifecycle.ViewModelProvider;

import com.example.allaround.databinding.FragmentRoundupBinding;

public class RoundupFragment extends Fragment {

    private FragmentRoundupBinding binding;

    public View onCreateView(@NonNull LayoutInflater inflater,
                             ViewGroup container, Bundle savedInstanceState) {
        RoundupViewModel roundupViewModel =
                new ViewModelProvider(this).get(RoundupViewModel.class);

        binding = FragmentRoundupBinding.inflate(inflater, container, false);
        View root = binding.getRoot();
//        for (int i = 0; i < 10; i++) {
//            ImageView imageView = new ImageView(this);
//            imageView.setId(i);
//            imageView.setPadding(2, 2, 2, 2);
//            imageView.setImageBitmap(BitmapFactory.decodeResource(
//                    getResources(), binding.drawable.ic_launcher));
//            imageView.setScaleType(ImageView.ScaleType.FIT_XY);
//            layout.addView(imageView);
//        }
        Switch switch1 = binding.switch1;
        Switch switch2 = binding.switch2;
        Switch switch3 = binding.switch3;
        TextView totalText = binding.textView2;
        totalText.setText("Total Donation: " + 0);
        double total = 0;





        final TextView textView = binding.textDashboard;
        roundupViewModel.getText().observe(getViewLifecycleOwner(), textView::setText);
        return root;

    }

    @Override
    public void onDestroyView() {
        super.onDestroyView();
        binding = null;
    }
}