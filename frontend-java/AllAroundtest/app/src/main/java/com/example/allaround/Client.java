package com.example.allaround;

import android.app.Application;

public class Client extends Application {
    private String name;
    private String email;
    private String password;
    private String bankName;
    private String bankId;
    private int montlyGoal;
    private int montlyDonation = 20;

    public static Client instance = new Client();

    public static Client getInstance(){
        return instance;
    }

    public void onCreate(){
        super.onCreate();
        instance = this;
    }

    

    public String getName(){
        return name;
    }

    public void setName(String name){
        this.name = name;
    }

    public String getEmail(){
        return email;
    }

    public void setEmail(String email){
        this.email = email;
    }

    public String getPassword(){
        return password;
    }

    public void setPassword(String password){
        this.password = password;
    }

    public String getBankName(){
        return bankName;
    }

    public void setBankName(String bankName){
        this.bankName = bankName;
    }

    public String getBankId(){
        return bankId;
    }

    public void setBankId(String bankName){
        this.bankId = bankId;
    }

    public int getMontlyGoal(){
        return montlyGoal;
    }

    public void setMontlyGoal(int montlyGoal){
        this.montlyGoal = montlyGoal;
    }

    public int getMontlyDonation(){
        return montlyDonation;
    }

    public void setMontlyDonation(int montlyDonation){
        this.montlyDonation = montlyDonation;
    }


}
