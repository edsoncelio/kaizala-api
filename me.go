package main

import (
	"fmt"
	"net/http"
	"io/ioutil"
)

func main() {

	url := "https://kms1.kaiza.la/v1/users/me"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("accessToken", "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cm46bWljcm9zb2Z0OmNyZWRlbnRpYWxzIjoie1wicGhvbmVOdW1iZXJcIjpcIis1NTg1OTk2MDU4NDAxXCIsXCJjSWRcIjpcIlwiLFwidGVzdFNlbmRlclwiOlwiZmFsc2VcIixcImFwcE5hbWVcIjpcImNvbS5taWNyb3NvZnQubW9iaWxlLmthaXphbGFhcGlcIixcImFwcGxpY2F0aW9uSWRcIjpcIjM3YmExZTQxLWQ1NWMtNDNiZi1hMmZhLWQ3MmM5N2FhMDgwYVwiLFwicGVybWlzc2lvbnNcIjpcIjIuMzA6My4zMDo2LjIyOjUuNDo5LjI6MTUuMzA6MTQuMzA6MTkuMzA6MjQuMzBcIixcImFwcGxpY2F0aW9uVHlwZVwiOjMsXCJkYXRhXCI6XCJ7XFxcIkFwcE5hbWVcXFwiOlxcXCJHTm90aWZpY2FcXFwifVwifSIsInVpZCI6Ik1vYmlsZUFwcHNTZXJ2aWNlOjc2MzQwM2IwLWI4N2YtNDM2Yi04MTI2LWM0NmQ1N2VlY2QyZkAxIiwidmVyIjoiMiIsIm5iZiI6MTU0NTIxNTQzNywiZXhwIjoxNTQ1MzAxODM3LCJpYXQiOjE1NDUyMTU0MzcsImlzcyI6InVybjptaWNyb3NvZnQ6d2luZG93cy1henVyZTp6dW1vIiwiYXVkIjoidXJuOm1pY3Jvc29mdDp3aW5kb3dzLWF6dXJlOnp1bW8ifQ.LKd1o35nfx8RilRnAZEirKXYuusYaqPFQLFUUON-H5w")
	req.Header.Add("cache-control", "no-cache")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := ioutil.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
