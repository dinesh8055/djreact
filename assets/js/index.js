var React = require('react')
var ReactDOM = require('react-dom')

var SavedJobsList = React.createClass({
    loadSavedJobsFromServer: function(){
        $.ajax({
            url: this.props.url,
            datatype: 'json',
            cache: false,
            success: function(data) {
                this.setState({data: data});
            }.bind(this)
        })
    },

    getInitialState: function() {
        return {data: []};
    },

    componentDidMount: function() {
        this.loadSavedJobsFromServer();
        setInterval(this.loadSavedJobsFromServer,
                    this.props.pollInterval)
    },
    render: function() {
        if (this.state.data) {
            console.log('DATA!')
            var savedJobNodes = this.state.data.map(function(savedJob){
                return <li> {savedJob.company+' : '+savedJob.title} </li>
            })
        }
        return (
            <div>
                <h1>Hello React!</h1>
                <ul>
                    {savedJobNodes}
                </ul>
            </div>
        )
    }
})

ReactDOM.render(<SavedJobsList url='/savedjobs/' pollInterval={1000} />,
    document.getElementById('container'))