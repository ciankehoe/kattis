/*
Problem: https://open.kattis.com/problems/wertyu
Author: Cian Kehoe
Submitted: July 1st, 2020
 */

package main

import (
	"fmt"
	"bufio"
	"os"
	"strings"
)

func main() {
	// string representation of keyboard
	keyboard := "1234567890-=QWERTYUIOP[]\\ASDFGHJKL;'ZXCVBNM,./"

	// create a new Scanner to read from stdin
	reader := bufio.NewScanner(os.Stdin)
	
	// keep reading lines from stdin until no more provided
	for reader.Scan() {
		text := reader.Text()
	
		// initialize output string
		output := ""
	
		// iterate through our scanned text from stdin
		for _, c := range text {
			// convert rune to string (individual letter)
			l := string(c)

			if strings.Contains(keyboard, l) {
				i := strings.Index(keyboard, l) // get index of letter in keyboard string
				leftLetter := string(keyboard[i-1])
				output = output + leftLetter
			} else {
				output += " " // spaces do not get converted
			}
		}
		fmt.Println(output)
	}
}