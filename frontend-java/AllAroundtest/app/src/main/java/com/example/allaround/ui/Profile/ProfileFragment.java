package com.example.allaround.ui.Profile;

import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.fragment.app.Fragment;
import androidx.lifecycle.ViewModelProvider;

import com.example.allaround.Client;
import com.example.allaround.databinding.FragmentProfileBinding;
import com.example.allaround.ui.Profile.ProfileViewModel;

import org.w3c.dom.Text;

public class ProfileFragment extends Fragment {

    private FragmentProfileBinding binding;

    public View onCreateView(@NonNull LayoutInflater inflater,
                             ViewGroup container, Bundle savedInstanceState) {
        ProfileViewModel notificationsViewModel =
                new ViewModelProvider(this).get(ProfileViewModel.class);

        binding = FragmentProfileBinding.inflate(inflater, container, false);
        View root = binding.getRoot();
        TextView viewName = binding.viewName;
        TextView viewBank = binding.viewBank;
        TextView viewGoal = binding.viewGoal;
        TextView viewDonation = binding.viewDonation;
        TextView viewStatus = binding.viewStatus;

        viewName.setText("Name: " + Client.getInstance().getName());
        viewBank.setText("Bank: " + Client.getInstance().getBankName());
        viewGoal.setText("Monthly Goal: $" + Client.getInstance().getMontlyGoal());
        viewDonation.setText("Current Donation: $" + Client.getInstance().getMontlyDonation());
        viewStatus.setText("Percentage achieved: %" + (int)(100.0 * Client.getInstance().getMontlyDonation() / Client.getInstance().getMontlyGoal()));


        final TextView textView = binding.textProfile;
        notificationsViewModel.getText().observe(getViewLifecycleOwner(), textView::setText);
        return root;
    }

    @Override
    public void onDestroyView() {
        super.onDestroyView();
        binding = null;
    }
}