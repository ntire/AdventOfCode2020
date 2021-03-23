package main

import (
	"bufio"
	"log"	
	"os"
)

func treecount(filename string, step_x int, step_y int) int{
	f, err := os.Open(filename)

	if err != nil {
		log.Fatal(err)
	}

	defer f.Close()

	scanner := bufio.NewScanner(f)

	var lines []string
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}

	pos_x := 0
	max_x := len(lines[0])
	tree_counter := 0

	for pos_y := 0; pos_y <= len(lines) - step_y; pos_y += step_y {
		symbol := lines[pos_y][pos_x]
		// fmt.Printf("symbol: %c\n", symbol)

		if symbol == '#' {
			tree_counter += 1
		}

		pos_x += step_x
		if pos_x >= max_x{
			pos_x -= max_x
		}
	}

	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}

	return tree_counter
}
