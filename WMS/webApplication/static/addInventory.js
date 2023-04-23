// AddInventory constructor.
class AddInventory extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      item: "",
      location: "",
      quantity: 0,
      items: [],
      locations: []
    };
    this.handleInputChange = this.handleInputChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

    // This method is called when a component is mounted.
  componentDidMount() {
    fetch("/api/items/")
      .then(response => response.json())
      .then(data => {
        this.setState({ items: data });
      });
    fetch("/api/locations/")
      .then(response => response.json())
      .then(data => {
        this.setState({ locations: data });
      });
  }

    // Handle input change.
  handleInputChange(event) {
    const target = event.target;
    const value = target.type === "checkbox" ? target.checked : target.value;
    const name = target.name;
    this.setState({
      [name]: value
    });
  }

    // Handle a submission.
  handleSubmit(event) {
    event.preventDefault();
    const csrftoken = this.getCookie('csrftoken');
    const data = {
      item: this.state.item,
      location: this.state.location,
      quantity: this.state.quantity
    };
      // Fetch data with CSRF token
    fetch("/api/inventory/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": csrftoken
      },
      body: JSON.stringify(data)
    })
      // Logs a JSON response.
      .then(response => response.json())
      .then(data => console.log(data))
      .catch(error => console.error(error));
      window.location.href = "/";
  }

    // Returns the cookie with the given name.
  getCookie(name) {
    var value = "; " + document.cookie;
    var parts = value.split("; " + name + "=");
    if (parts.length == 2) return parts.pop().split(";").shift();
  }


    render() {
      return (
        <div className="container col-5 p-5">
          <h1 className = "p-5">Add Inventory</h1>
          <form onSubmit={this.handleSubmit}>
            <div className="form-group">
              <label htmlFor="item">Item:</label>
              <select
                className="form-control"
                id="item"
                name="item"
                value={this.state.item}
                onChange={this.handleInputChange}
              >
                <option value="">Select an item</option>
                {this.state.items.map(item => (
                  <option key={item.id} value={item.id}>
                    {item.name}
                  </option>
                ))}
              </select>
            </div>
            <div className="form-group">
              <label htmlFor="location">Location:</label>
              <select
                className="form-control"
                id="location"
                name="location"
                value={this.state.location}
                onChange={this.handleInputChange}
              >
                <option value="">Select a location</option>
                {this.state.locations.map(location => (
                  <option key={location.id} value={location.id}>
                    {location.name}
                  </option>
                ))}
              </select>
            </div>
            <div className="form-group">
              <label htmlFor="quantity">Quantity:</label>
              <input
                className="form-control"
                id="quantity"
                name="quantity"
                type="number"
                value={this.state.quantity}
                onChange={this.handleInputChange}
              />
            </div>
            <button type="submit" className="btn btn-primary" >Add Inventory</button>
          </form>
        </div>
      );
    }
    
  }
ReactDOM.render(<AddInventory />, document.getElementById("root"));
