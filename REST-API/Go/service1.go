// Seriál "Programovací jazyk Go"
//
// Dvanáctá část
//
// Demonstrační příklad číslo 1:
//    Jednoduchý HTTP server

package main

import (
	"io"
	"net/http"
)

func mainEndpoint(writer http.ResponseWriter, request *http.Request) {
	io.WriteString(writer, "Hello world!\n")
}

func main() {
	http.HandleFunc("/", mainEndpoint)
	http.ListenAndServe(":8000", nil)
}
