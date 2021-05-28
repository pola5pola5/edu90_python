package main

// よく分からなくてerrのまま
import (
	"fmt"
)

func main() {
	var H, W int
	fmt.Scanf("%d", &H)
	fmt.Scanf("%d", &W)

	var A [][]int
	for i := 0; i < H; i++ {
		for j := 0; j < W; j++ {
			fmt.Scanf("%d", &A[i][j])
		}
	}
	fmt.Println(A)
}
