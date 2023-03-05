package com.example.allaround.ui.home;

import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ImageView;
import android.widget.ProgressBar;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.fragment.app.Fragment;
import androidx.lifecycle.ViewModelProvider;

import com.example.allaround.Client;
import com.example.allaround.databinding.FragmentHomeBinding;

public class HomeFragment extends Fragment {

    private FragmentHomeBinding binding;

    public View onCreateView(@NonNull LayoutInflater inflater,
                             ViewGroup container, Bundle savedInstanceState) {
        HomeViewModel homeViewModel =
                new ViewModelProvider(this).get(HomeViewModel.class);

        binding = FragmentHomeBinding.inflate(inflater, container, false);
        View root = binding.getRoot();
        ProgressBar progressBar = binding.simpleProgressBar;
        ImageView snail = binding.snail;

        snail.setX((float)(20 + 950.0 * Client.getInstance().getMontlyDonation() / Client.getInstance().getMontlyGoal()));


        if(Client.getInstance().getMontlyGoal() > 0)
            progressBar.setProgress((int)(100.0 * Client.getInstance().getMontlyDonation() / Client.getInstance().getMontlyGoal()));
        final TextView textView = binding.textHome;
        homeViewModel.getText().observe(getViewLifecycleOwner(), textView::setText);
        return root;
    }

    @Override
    public void onDestroyView() {
        super.onDestroyView();
        binding = null;
    }
}