class AddInventory extends React.Component {
    constructor(props) {
      super(props);
      this.state = {
        item: "",
        location: "",
        quantity: "",
        message: "",
      };
      this.handleSubmit = this.handleSubmit.bind(this);
      this.handleItemChange = this.handleItemChange.bind(this);
      this.handleLocationChange = this.handleLocationChange.bind(this);
      this.handleQuantityChange = this.handleQuantityChange.bind(this);
    }

    handleItemChange(event) {
      this.setState({ item: event.target.value });
    }

    handleLocationChange(event) {
      this.setState({ location: event.target.value });
    }

    handleQuantityChange(event) {
      this.setState({ quantity: event.target.value });
    }

    handleSubmit(event) {
      event.preventDefault();
      // Make API call to add inventory
      fetch("/api/inventory/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          quantity: this.state.quantity,
          item: this.state.item,
          location: this.state.location,          
        }),
      })
        .then((response) => {
          if (!response.ok) {
            throw new Error("Network response was not ok");
          }
          return response.json();
        })
        .then((data) => {
          this.setState({
            message: `Successfully added ${data.quantity} of ${data.item} to ${data.location}`,
          });
        })
        .catch((error) => {
          console.error("Error:", error);
          this.setState({
            message: `Failed to add inventory: ${error.message}`,
          });
        });
    }

    render() {
      return (
        <form onSubmit={this.handleSubmit}>
          <label>
            Item:
            <input
              type="text"
              value={this.state.item}
              onChange={this.handleItemChange}
            />
          </label>
          <br />
          <label>
            Location:
            <input
              type="text"
              value={this.state.location}
              onChange={this.handleLocationChange}
            />
          </label>
          <br />
          <label>
            Quantity:
            <input
              type="number"
              value={this.state.quantity}
              onChange={this.handleQuantityChange}
            />
          </label>
          <br />
          <input type="submit" value="Submit" />
          <div>{this.state.message}</div>
        </form>
      );
    }
  }

  ReactDOM.render(<AddInventory />, document.getElementById("root"));