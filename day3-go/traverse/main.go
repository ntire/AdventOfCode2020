package main

import (
	"fmt"
)

func main() {
	treecount := treecount("../input", 3, 1)
	fmt.Printf("Counted %d trees\n", treecount)
}