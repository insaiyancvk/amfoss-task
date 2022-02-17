class Github {

  constructor() {

    this.client_id = '';
    this.client_secret = '';
    this.count = 5;
    this.repos_sort = 'created: asc';

  }

  async getUser(user) {

    const profileResponse = await fetch(`https://api.github.com/users/${user}?client_id=${this.client_id}&client_secret=${this.client_secret}`);
    const profile = await profileResponse.json();
    return {profile}

  }
  
}
