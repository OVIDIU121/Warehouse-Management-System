class InventoryTable extends React.Component {
    constructor(props) {
      super(props);
      this.state = { inventory: [] };
    }
  
    componentDidMount() {
      this.loadInventory();
    }
  
    loadInventory() {
      fetch("api/inventory/")
        .then((response) => response.json())
        .then((data) => {
          this.setState({ inventory: data });
        });
    }
  
    handleDelete(id) {
      if (!confirm("Are you sure you want to delete this item?")) {
        return;
      }
      fetch(`api/inventory/${id}/`, {
        method: "DELETE",
        headers: {
          "Content-Type": "application/json",
          Accept: "application/json",
        },
      })
        .then(() => {
          this.loadInventory();
        })
        .catch((error) => console.error(error));
    }
  
    renderInventory() {
      return (
        <table className="table table-striped">
          <thead>
            <tr>
              <th>Item Name</th>
              <th>Location Name</th>
              <th>Quantity</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            {this.state.inventory.map((item) => (
              <tr key={item.id}>
                <td>{item.item.name}</td>
                <td>{item.location.name}</td>
                <td>{item.quantity}</td>
                <td>
                  <button
                    type="button"
                    className="btn btn-danger"
                    onClick={() => this.handleDelete(item.id)}
                  >
                    Delete
                  </button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      );
    }
  
    render() {
      return (
        <div>
          <h1>Inventory</h1>
          <button
            type="button"
            className="btn btn-primary"
            onClick={() => this.loadInventory()}
          >
            Query
          </button>
          <button type="button" className="btn btn-success">
            Add
          </button>
          {this.renderInventory()}
        </div>
      );
    }
  }
  
  ReactDOM.render(<InventoryTable />, document.getElementById("root"));
  