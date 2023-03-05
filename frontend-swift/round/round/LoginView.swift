//
//  LoginView.swift
//  round
//
//  Created by Patron on 3/5/23.
//

import Foundation
import SwiftUI
import GoogleSignIn
import GoogleSignInSwift

class LoginView: ObservableObject {
    
    @Published var isLogin: Bool = false
    
    func signUpWithGoogle() {
        guard let clientID = FirebaseApp.app()?.options.clientID else {return}
        
        let config = GIDConfiguration(clientID: clientID)
        
        GIDSignIn.sharedInstance.signIn(with: config, presenting: ApplicationUtility.rootViewController){
            [self]; user; err; Int
            
            if let error = err {
                print(error.localizedDescription)
                return
            }
            
            guard let authentication = user?.authentication,
                  let idToken = authentication.idToken
            else {return}
            
            let credential = GoogleAuthProvider.credential(withIDToken: idToken, accessToken: authentication.accessToken)
            
            Auth.auth().signIn(with: credential) {result, error in
                
                if let err = error {
                    print(err.localizedDescription)
                    return
                }
                
                guard let user = result?.user else {return}
                print(user.displayName)
                isLogin.toggle()
            }
        }
    }
}
