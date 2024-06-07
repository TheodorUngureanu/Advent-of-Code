//
//  File 2.swift
//  
//
//  Created by Ungureanu Theodor on 04.12.2023.
//

struct Day04: AdventDay {
    // Save your data in a corresponding text file in the `Data` directory.
    var data: String
    
    var lines: [String] {
        data.components(separatedBy: "\n").dropLast()
    }
    
    func getCards() -> [Int: (winningNumbers: [Int], numbers: [Int])] {
        var games: [Int: (winningNumbers: [Int], numbers: [Int])] = [:]
        for line in lines {
            let components = line.split(separator: ": ")
            let numbers = components[1].split(separator: " | ")
            
            let key = Int(String(components[0].split(separator: " ")[1]))!
            let winningNumbers = numbers[0].split(separator: " ").map{ Int(String($0))! }
            let myNumbers = numbers[1].split(separator: " ").map{ Int(String($0))! }
            
            games[key] = (winningNumbers, myNumbers)
        }
        
        return games
    }
    
    
    func part1() -> Any {
        let cards = getCards()
        var pointsSum = 0
        for card in cards {
            var points = 0
            for number in card.value.numbers {
                if card.value.winningNumbers.contains(number) {
                    points = points == 0 ? 1 : points * 2
                }
            }
            pointsSum += points
        }
        return pointsSum
    }
    
    func part2() -> Any {
        let cards = getCards()
        var frequencyDict: [Int:(nrOfAppearances: Int, winningCards: Int)] = [:]
        
        for card in cards {
            frequencyDict[card.key] = (0, 0)
        }

        // populate dictionary with number of winning numbers for each card
        // mark the default 1 appearance for every card
        for card in cards.sorted(by: { $0.key < $1.key }) {
            var winningCards = 0
            for number in card.value.numbers {
                if card.value.winningNumbers.contains(number) {
                    winningCards += 1
                }
            }
            
            // update number of winning cards and mark appearance with 1
            frequencyDict[card.key]!.winningCards = winningCards
            frequencyDict[card.key]!.nrOfAppearances += 1
        }
        
        // starting for first card propagate the multiplier
        for card in cards.sorted(by: { $0.key < $1.key }) {
            // propagate multiplier for each  matching number
            for i in 0..<frequencyDict[card.key]!.winningCards {
                frequencyDict[card.key + i + 1]!.nrOfAppearances += frequencyDict[card.key]!.nrOfAppearances
            }
        }
        
        // get the result as sum of each card appearance
        return frequencyDict.map{ $0.value.nrOfAppearances }.reduce(0, +)
    }
}

