function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
      const cookies = document.cookie.split(';');
      for (let i = 0; i < cookies.length; i++) {
          const cookie = cookies[i].trim();
          // Does this cookie string begin with the name we want?
          if (cookie.substring(0, name.length + 1) === (name + '=')) {
              cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
              break;
          }
      }
  }
  return cookieValue;
}

class InventoryList extends React.Component {
  
    state = {
      inventories: [],
    };
  
    componentDidMount() {
      this.fetchInventories();
    }

    handleDelete(id) {
      //const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
      if (!confirm("Are you sure you want to delete this item?")) {
        return;
      }
      fetch(`api/inventory/${id}/`, {
        method: "DELETE",
        headers: {
          'Content-Type': 'application/json',
          'X-CSRFToken': getCookie('csrftoken')
        },
      })
        .then(() => {
          this.fetchInventories();
        })
        .catch((error) => console.error(error));
    }
  
    fetchInventories = () => {
      fetch("/api/inventory/")
        .then((res) => res.json())
        .then((data) => {
          const promises = data.map((inventory) => {
            const itemPromise = fetch(`/api/items/${inventory.item}/`).then((res) =>
              res.json()
            );
            const locationPromise = fetch(
              `/api/locations/${inventory.location}/`
            ).then((res) => res.json());
  
            return Promise.all([itemPromise, locationPromise]).then(
              ([itemData, locationData]) => ({
                ...inventory,
                itemName: itemData.name,
                locationName: locationData.name,
              })
            );
          });
  
          Promise.all(promises).then((inventories) =>
            this.setState({ inventories })
          );
        });
    };
  
    render() {
      const { inventories } = this.state;
  
      return (
        <div className="vh-100 d-flex justify-content-center align-items-center">
          <div className="container">
            <div className="row d-flex justify-content-center"></div>
                <h2 className="fw-bold mb-2 text-uppercase">
                Inventory List
                </h2>
                  <table className="table table-striped table-hover" >
                    <thead>
                      <tr>
                        <th>Location</th>
                        <th>Item</th>
                        <th>Quantity</th>
                        <th>Action</th>
                      </tr>
                    </thead>
                    <tbody>
                      {inventories.map((inventory) => (
                        <tr key={inventory.id}>
                          <td>{inventory.locationName}</td>
                          <td>{inventory.itemName}</td>
                          <td>{inventory.quantity}</td>
                          <td>
                          <div className="btn-toolbar " role="group" aria-label="Basic example">
                          <div className="btn btn-group " role="group" aria-label="First group">
                          <button type="button" className="btn btn-secondary">Edit</button>
                          </div>
                          <div className="btn btn-group" role="group" aria-label="Second group">
                          <button type="button" class="btn btn-danger" onClick={() => this.handleDelete(inventory.id)}>Delete</button>
                          </div>
                        </div>

                          </td>
                        </tr>
                      ))}
                    </tbody>
                  </table>
            </div>
        </div>        
      );
    }
  }

  ReactDOM.render(<InventoryList />, document.getElementById("root"));