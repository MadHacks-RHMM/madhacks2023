//
//  ActualLoginView.swift
//  round
//
//  Created by Patron on 3/5/23.
//

import SwiftUI

struct ActualLoginView: View {
    @EnvironmentObject var loginVM: LoginView
    
    var body: some View {
        Button{
            loginVM.signUpWithGoogle()
        } label: {
            Text("google button")
        }
    }
}
