package com.example.allaround.ui.roundup;

import androidx.lifecycle.LiveData;
import androidx.lifecycle.MutableLiveData;
import androidx.lifecycle.ViewModel;

public class RoundupViewModel extends ViewModel {

    private final MutableLiveData<String> mText;

    public RoundupViewModel() {
        mText = new MutableLiveData<>();
        mText.setValue("Wrapupped!");
    }

    public LiveData<String> getText() {
        return mText;
    }
}