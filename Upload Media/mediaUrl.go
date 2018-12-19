package main

import (
	"fmt"
	"strings"
	"net/http"
	"io/ioutil"
)

func main() {

	url := "https://api.kaiza.la/v1/media/url"

	payload := strings.NewReader("{mediaUrl:\"https://manage.kaiza.la/Images/landing-images/main-page-1.png\"}")

	req, _ := http.NewRequest("POST", url, payload)

	req.Header.Add("accessToken", "")
	req.Header.Add("Content-Type", "application/json")
	req.Header.Add("cache-control", "no-cache")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := ioutil.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}