package main

import (
	"fmt"
	"strings"
	"net/http"
	"io/ioutil"
)

func main() {

	url := "https://api.kaiza.la/v1/loginWithPinAndApplicationId"

	payload := strings.NewReader("{\"mobileNumber\":\"+5585996058401\",\"applicationId\":\"37ba1e41-d55c-43bf-a2fa-d72c97aa080a\", \"applicationSecret\":\"W2N7H1RW3V\", \"pin\":6823}")

	req, _ := http.NewRequest("POST", url, payload)

	req.Header.Add("Content-Type", "application/json")
	req.Header.Add("cache-control", "no-cache")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := ioutil.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
