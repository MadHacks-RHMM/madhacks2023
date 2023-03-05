//
//  ContentView.swift
//  round
//
//  Created by Patron on 3/4/23.
//

import SwiftUI

struct ContentView: View {
    
    @EnvironmentObject var loginView: LoginView
    
    var body: some View {
        NavigationView {
            GeometryReader { geometry in
                ZStack(alignment: .center) {
                    Image("homeback")
                        .resizable()
                        .aspectRatio(contentMode: .fill)
                        .frame(width: geometry.size.width, height: geometry.size.height)
                        .clipped()
                        .ignoresSafeArea()
                    VStack(alignment: .center) {
                        Image("loginsym")
                            .imageScale(.large)
                            .offset(y: -150)
                        NavigationLink(destination: LoginView()) {
                            Text("login")
                                .bold()
                                .frame(width: 200, height: 50)
                                .background(Color(red: 0, green: 0, blue: 0))
                                .foregroundColor(Color.white)
                        }
                        .offset(y: -100)
                    }
                }
            }
        }
        .padding()
    }
}
struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}
