package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"net/http"

	"github.com/gin-gonic/gin"
)

type AutoGenerated struct {
	data []string `json:"data"`
}

func main() {
	router := gin.Default()
	router.GET("/", data)

	router.Run("localhost:8080")
}

func data(c *gin.Context) {
	raw, err := ioutil.ReadFile("data.json")
	if err != nil {
		fmt.Println(err)
	}
	var test AutoGenerated
	lol, err := json.Unmarshal(raw, &test)

	c.IndentedJSON(http.StatusOK, lol)
}
