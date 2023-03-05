package com.example.allaround;

import android.app.Application;

public class Charity extends Application {

    private String name;
    private String description;
    private String venmoID;

    public static Charity instance = new Charity();

    public static Charity getInstance(){
        return instance;
    }

    public void onCreate(){
        super.onCreate();
        instance = this;
    }

    public void setName(String name) {
        this.name = name;
    }

    public void setDesc(String description){
        this.description = description;
    }

    public void setVID(String VID){
        this.venmoID = VID;
    }

    public String getName(){
        return name;
    }

    public String getDescription(){
        return description;
    }

    public String getVenmoID(){
        return venmoID;
    }



}
