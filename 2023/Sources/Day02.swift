//
//  File.swift
//
//
//  Created by Ungureanu Theodor on 01.12.2023.
//

struct Day02: AdventDay {
    // Save your data in a corresponding text file in the `Data` directory.
    var data: String
    
    var entities: [String] {
        data.components(separatedBy: "\n").dropLast()
    }
    
    func part1() -> Any {
        // valid games
        var sumValidGames = 0
        // dictionary with key=game value=cubes
        var dict: [String: [String]] = [:]
        for line in entities {
            let parts = line.components(separatedBy: ": ")
            dict[parts[0]] = parts[1].components(separatedBy: "; ")
        }
        
        // validate games
        for (key, values) in dict {
            //            print("GAME: \(key)")
            var gameValid = true
            for subset in values {
                // initial values
                var redCubes = 12
                var greenCubes = 13
                var blueCubes = 14
                //                print(subset)
                let cubes = subset.components(separatedBy: ", ")
                for cube in cubes {
                    let values = cube.components(separatedBy: " ")  // (value, cube color)
                    switch values[1] {
                    case "red":
                        redCubes -= Int(values[0])!
                    case "green":
                        greenCubes -= Int(values[0])!
                    case "blue":
                        blueCubes -= Int(values[0])!
                    default:
                        print("Incorrect value: \(values[1])")
                        return 0
                    }
                }
                // check if round is valid
                if redCubes < 0 || greenCubes < 0 || blueCubes < 0 {
                    gameValid = false
                    continue
                }
            }
            if gameValid {
                sumValidGames += Int(key.components(separatedBy: " ")[1])!
            }
            
        }
        return sumValidGames
    }
    
    func part2() -> Any {
        // dictionary with key=game value=cubes
        var dict: [String: [String]] = [:]
        for line in entities {
            let parts = line.components(separatedBy: ": ")
            dict[parts[0]] = parts[1].components(separatedBy: "; ")
        }
        
        var sumGamePower = 0
        // validate games
        for (_, values) in dict {
            var (maxRed, maxGreen, maxBlue) = (0,0,0)
            for subset in values {
                let cubes = subset.components(separatedBy: ", ")
                for cube in cubes {
                    let values = cube.components(separatedBy: " ")  // (value, cube color)
                    switch values[1] {
                    case "red":
                        maxRed = Int(values[0])! > maxRed ? Int(values[0])! : maxRed
                    case "green":
                        maxGreen = Int(values[0])! > maxGreen ? Int(values[0])! : maxGreen
                    case "blue":
                        maxBlue = Int(values[0])! > maxBlue ? Int(values[0])! : maxBlue
                    default:
                        print("Incorrect value: \(values[1])")
                        return 0
                    }
                }
            }
            sumGamePower += maxRed * maxGreen * maxBlue
        }
        return sumGamePower
    }
}
