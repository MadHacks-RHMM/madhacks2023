//
//  Application.swift
//  round
//
//  Created by Patron on 3/5/23.
//

import SwiftUI

final class ApplicationUtility {
    
    static var rootViewController: UIViewController {
        
        guard let screen = UIApplication.shared.connectedScenes.first as? UIWindowsScene else {
            return .init()
        }
        
        guard let root = screen.windows.first.rootViewController else {
            return .init()
        }
        
        return root
    }
}
