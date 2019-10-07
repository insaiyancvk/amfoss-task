package main

import (

    "github.com/dghubble/go-twitter/twitter"
    "github.com/dghubble/oauth1"
    "os"
    "flag"
    "fmt"
	
)

func main() {

	config := oauth1.NewConfig("<API Key>", "<API Secret Key>") //API Key and API Secret Key

	token := oauth1.NewToken("Access Token", "Access Token Secret") //Access Token and Access Token Secret
	
	httpClient := config.Client(oauth1.NoContext, token) //requesting for access
	
	client := twitter.NewClient(httpClient) //Twitter Client
	
	var username string //Variable for username

	var c int = 0 //variable for counting the number of followers

	fmt.Println("Enter the user handle to fetch the number of followers :")
	fmt.Scanln(&username)
	
	fetch := flag.String("",username,"") // define the username as flag

	flag.Parse() // calling the flag
    
	foo, err := os.Create("Followers Of "+username+".txt") // creates the text file as "Followers Of <username>"

	followers, resp, err := client.Followers.List(&twitter.FollowerListParams{ScreenName: *fetch}) // gets the information of the followers of the given username

	fmt.Println(resp, err) // as the error "err declared and not used" and "resp declared and not used" was popping up, it prints
	

	foo.WriteString("Followers of @" + username + "\n") // Writes in the text file
	

	for _, follower := range followers.Users{ 

		c++

		foo.WriteString("\n"+follower.ScreenName+"\n") //Writes each follower username to the text file

		}
	foo.WriteString("\n\n")
	
	foo.WriteString("The number of followers of @") //as the error "too many arguments in call to foo.WriteString" was showing up, I had to write each division seperately to the file

	foo.WriteString(username)

	foo.WriteString(" are ")

	foo.WriteString(fmt.Sprintf("%d\n",c)) //Writes the counted number of followers in the loop to the text file

    foo.Close()
}
