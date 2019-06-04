import React, {Component} from 'react'
import {get} from '../../helpers/request-handler'
import {Container}from 'semantic-ui-react'
import {Segment, Dimmer, Loader}from 'semantic-ui-react'
import SearchBarComponent from './components/SearchBarComponent'
import SearchResultsComponent from './components/SearchResultsComponent'
import UnversitiesDropdownComponent from './components/UniversitiesDropdownComponent'


export default class SearchComponent extends Component {
    constructor() {
        super()
        this.state = {queryData: [], isQueryLoading: false, cities: []}
        this.queryHandler = this.queryHandler.bind(this)
    }

    componentDidMount() {
        this.fetchCities()
    }

    async fetchCities(){
        const res = await get(`/cities`)
        res.data && this.setState({cities : res.data})
    }

    async queryHandler(query, city) {
        this.setState({isQueryLoading: true})
        const res = await get(`/query?query=${query}&city=${city}`)
        this.setState({isQueryLoading: false, queryData: res.data || []})
    }

    render() {
        return (
            <Container>
                <SearchBarComponent
                    cities = {this.state.cities}
                    queryHandler={ this.queryHandler }
                />

                <UnversitiesDropdownComponent
                    universities={this.state.queryData.map(obj => obj.university_name)}/>
                <br/>

                <Container fluid>
                    <Loader active={this.state.isQueryLoading}></Loader>
                </Container>

                <Dimmer.Dimmable as={Segment} blurring dimmed={this.state.isQueryLoading}>
                    <SearchResultsComponent queryRespData={this.state.queryData}/>
                </Dimmer.Dimmable>
            </Container>
        )
    }
}
