package main

import (
	"fmt"
	"net/http"
	"io/ioutil"
)

func main() {

	url := "https://api.kaiza.la/v1/accessToken"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("applicationId", "37ba1e41-d55c-43bf-a2fa-d72c97aa080a")
	req.Header.Add("applicationSecret", "W2N7H1RW3V")
	req.Header.Add("refreshToken", "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cm46bWljcm9zb2Z0OmNyZWRlbnRpYWxzIjoie1wicGhvbmVOdW1iZXJcIjpcIis1NTg1OTk2MDU4NDAxXCIsXCJjSWRcIjpcIlwiLFwidGVzdFNlbmRlclwiOlwiZmFsc2VcIixcImFwcE5hbWVcIjpcImNvbS5taWNyb3NvZnQubW9iaWxlLmthaXphbGFhcGlcIixcImFwcGxpY2F0aW9uSWRcIjpcIjM3YmExZTQxLWQ1NWMtNDNiZi1hMmZhLWQ3MmM5N2FhMDgwYVwiLFwicGVybWlzc2lvbnNcIjpcIjguNFwiLFwiYXBwbGljYXRpb25UeXBlXCI6LTEsXCJkYXRhXCI6XCJ7XFxcIkFwcE5hbWVcXFwiOlxcXCJHTm90aWZpY2FcXFwifVwifSIsInVpZCI6Ik1vYmlsZUFwcHNTZXJ2aWNlOjc2MzQwM2IwLWI4N2YtNDM2Yi04MTI2LWM0NmQ1N2VlY2QyZkAxIiwidmVyIjoiMiIsIm5iZiI6MTU0NTIxNTQzNywiZXhwIjoxNTc2NzUxNDM3LCJpYXQiOjE1NDUyMTU0MzcsImlzcyI6InVybjptaWNyb3NvZnQ6d2luZG93cy1henVyZTp6dW1vIiwiYXVkIjoidXJuOm1pY3Jvc29mdDp3aW5kb3dzLWF6dXJlOnp1bW8ifQ.RKiI4Oej3R-7NnVxVS24LaUdKMlC1TkgUKNdv-iX1g4")
	req.Header.Add("cache-control", "no-cache")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := ioutil.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
