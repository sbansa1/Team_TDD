import React,{Component} from 'react';
import ReactDOM from 'react-dom';
import axios from 'axios';
import UsersList from './components/UsersList';
import AddUser from './components/AddUser';



class App extends Component {
 constructor() {
  super();

  // new
  this.state = {
    users: [],
    username: "",
    email: "",
  };

  this.addUser = this.addUser.bind(this);
  this.handleChange = this.handleChange.bind(this);
};
  // new
  componentDidMount() {
    this.getUsers();
  };
addUser(event) {
  event.preventDefault();

  const data = {
    username: this.state.username,
    email: this.state.email
  };

  axios.post(`http://localhost:5001/user/users`, data)
  .then((res) => {
    this.getUsers();  // new
    this.setState({ username: '', email: '' });  // new
  })
  .catch((err) => { console.log(err); });
};


  getUsers() {
    axios.get(`http://localhost:5001/user/users`)
    .then((res) => {this.setState({users: res.data}); })
    .catch((err) => { console.log(err); });
  };


  handleChange(event){
  const obj = {};
  obj[event.target.name] = event.target.value
  this.setState(obj);
  };



  render() {
  return (
    <section className="section">
      <div className="container">
        <div className="columns">
          <div className="column is-one-third">
            <br/>
            <h1 className="title is-1">Users</h1>
            <hr/><br/>
            <AddUser
            username = {this.state.username}
            email = {this.state.email}
            addUser={this.addUser}
            handleChange={this.handleChange}/>
            <br/><br/>
            <UsersList users={this.state.users}/>
          </div>
        </div>
      </div>
    </section>
  )
}
};

ReactDOM.render(
  <App />,
  document.getElementById('root')
);

