//
//  File.swift
//  
//
//  Created by Ungureanu Theodor on 04.12.2023.
//

struct Dayx: AdventDay {
    // Save your data in a corresponding text file in the `Data` directory.
    var data: String
    
    var lines: [String] {
        data.components(separatedBy: "\n").dropLast()
    }
    
    func part1() -> Any {
        return 0
    }
    
    func part2() -> Any {
        return 0
    }
}
