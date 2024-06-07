//
//  File.swift
//
//
//  Created by Ungureanu Theodor on 01.12.2023.
//

struct Day01: AdventDay {
    // Save your data in a corresponding text file in the `Data` directory.
    var data: String
    
    var entities: [String] {
        data.components(separatedBy: "\n")
    }
    
    func part1() -> Any {
        entities.map { word in
            let digit1: Int = word.first { $0.isNumber }?.wholeNumberValue ?? 0
            let digit2: Int = word.reversed().first { $0.isNumber}?.wholeNumberValue ?? 0
            return digit1 * 10 + digit2
        }.reduce(0, +)
    }
    
    func part2() -> Any {
        let sanitiedInput = entities.map { word in
            var newWord = word
            newWord = newWord.replacingOccurrences(of: "one", with: "one1one")
            newWord = newWord.replacingOccurrences(of: "two", with: "two2two")
            newWord = newWord.replacingOccurrences(of: "three", with: "three3three")
            newWord = newWord.replacingOccurrences(of: "four", with: "four4four")
            newWord = newWord.replacingOccurrences(of: "five", with: "five5five")
            newWord = newWord.replacingOccurrences(of: "six", with: "six6six")
            newWord = newWord.replacingOccurrences(of: "seven", with: "seven7seven")
            newWord = newWord.replacingOccurrences(of: "eight", with: "eight8eight")
            newWord = newWord.replacingOccurrences(of: "nine", with: "nine9nine")
            return newWord
        }
        // get the digits and return result
        return sanitiedInput.map { word in
            let digit1: Int = word.first { $0.isNumber }?.wholeNumberValue ?? 0
            let digit2: Int = word.reversed().first { $0.isNumber}?.wholeNumberValue ?? 0
            return digit1 * 10 + digit2
        }.reduce(0, +)
    }
}
