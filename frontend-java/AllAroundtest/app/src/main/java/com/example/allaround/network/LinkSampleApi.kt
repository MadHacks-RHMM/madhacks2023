package com.example.allaround.network

import com.google.gson.annotations.SerializedName
import io.reactivex.rxjava3.core.Single
import retrofit2.http.POST

/**
 * API calls to our localhost token server.
 */
/**
 * Implemented with reference from https://github.com/plaid/plaid-link-android.git
 * including res/value/strings.xml, network/LinkSampleApi.kt, network/LinkTokenRequester
 */
interface LinkSampleApi {

  @POST("/api/create_link_token")
  fun getLinkToken(): Single<LinkToken>
}

data class LinkToken(
  @SerializedName("link_token") val link_token: String
)

