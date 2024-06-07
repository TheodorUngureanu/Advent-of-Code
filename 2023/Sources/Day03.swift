//
//  File.swift
//  
//
//  Created by Ungureanu Theodor on 04.12.2023.
//

import Foundation

struct Day03: AdventDay {
    // Save your data in a corresponding text file in the `Data` directory.
    var data: String
    
    var lines: [String] {
        data.components(separatedBy: "\n").dropLast()
    }
    
    func part1() -> Any {
        let grid = lines.map { $0.split(separator: "") }
        print(grid)
        let directions = [[0,1], [1,0], [0,-1], [-1, 0], [-1,1], [-1,-1], [1,-1], [1,1]]
        
        var partNumberSum = 0
        let maxX = lines[0].count
        let maxY = lines.count
        
        
        for (i, line) in lines.enumerated() {
            var digits: String = ""
            var adjacent = false
            
            for (j, char) in line.enumerated() {
                if char.isNumber {
//                    print("char: \(char)")
                    digits.append(char)
                    
                    // we already know this number is adjacent to a symbol
                    if adjacent {
                        continue
                    }
                    
                    // search for adjacent symbols
                    for direction in directions {
                        let x = i + direction[0]
                        let y = j + direction[1]
                        
                        // if we are inside grid we continue
                        if 0..<maxX ~= x && 0..<maxY ~= y {
                            let symbolChar: String = String(grid[x][y])
                            
//                            print("x: \(x) y: \(y) symbol \(symbolChar)")
//                            print("Digits: \(digits)")
                            // validate symbol
                            if !adjacent && symbolChar != "." && !"0123456789".contains(symbolChar) {
                                adjacent = true
//                                print("dada")
//                                break
                            }
                        }
                    }
                } else {
                    if adjacent {
                        print(digits)
                        partNumberSum += Int(digits)!
                    }
                    digits = ""
                    adjacent = false
                }
            }
        }
        return partNumberSum
    }
    
    func part2() -> Any {
        return 0
    }
}
