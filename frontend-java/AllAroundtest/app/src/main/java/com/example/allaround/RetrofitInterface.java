package com.example.allaround;

import java.util.HashMap;

import retrofit2.Call;
import retrofit2.http.Body;
import retrofit2.http.POST;
public interface RetrofitInterface {

    /**
     * Login HTTP protocol for calling information from Login
     * @param map: input of name and email
     * @return boolean
     */
    @POST("/login")
    Call<Boolean> executeLogin(@Body HashMap<String, String> map);





}