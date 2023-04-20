// define the Receiving component
class Receiving extends React.Component {
    constructor(props) {
      super(props);
      // initialize the state with empty values
      this.state = {
        preadviceId: '',
        itemId: '',
        quantity: '',
        locationId: '',
        message: ''
      };
    }
  
    // handle input changes and update the state
    handleInputChange = (event) => {
      const target = event.target;
      const value = target.type === 'checkbox' ? target.checked : target.value;
      const name = target.name;
  
      this.setState({
        [name]: value
      });
    }
  
    // handle form submission
    handleSubmit = (event) => {
      event.preventDefault();
  
      // send a POST request to the server to receive the item
      fetch('/api/preadvice-items/1', {
        method: 'PUT',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            id: 1,
            preadvice_status: "R",
            expected_quantity: 1,
            received_quantity: 1,
            preadvice: 1,
            item: "sadasdasdas",
            received_location: 1
        })
      })
      .then(response => response.json())
      .then(data => {
        // display a success or error message
        this.setState({message: data.message});
      })
      .catch(error => {
        console.error('Error:', error);
      });
    }
  
    // render the Receiving component
    render() {
      return (
        <div>
          <h1>Adding preadvice</h1>
          <form onSubmit={this.handleSubmit}>
            <label>
              Pre-Advice ID:
              <input type="text" name="preadviceId" value={this.state.preadviceId} onChange={this.handleInputChange} />
            </label><br />
            <label>
              Item ID:
              <input type="text" name="itemId" value={this.state.itemId} onChange={this.handleInputChange} />
            </label><br />
            <label>
              Quantity:
              <input type="number" name="quantity" value={this.state.quantity} onChange={this.handleInputChange} />
            </label><br />
            <label>
              Location ID:
              <input type="text" name="locationId" value={this.state.locationId} onChange={this.handleInputChange} />
            </label><br />
            <input type="submit" value="Receive Item" />
          </form>
          <p>{this.state.message}</p>
        </div>
      );
    }
  }
  
  ReactDOM.render(
    <Receiving />,
    document.getElementById('root')
  );
  