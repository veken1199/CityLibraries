import axios from 'axios'
import React, {Component} from 'react'
import {get} from '../../helpers/request-handler'
import {Container, Sticky}from 'semantic-ui-react'
import {Input, Segment, Button, Dimmer, Loader}from 'semantic-ui-react'
import SearchBarComponent from './components/SearchBarComponent'
import SearchResultsComponent from './components/SearchResultsComponent'
import UnversitiesDropdownComponent from './components/UniversitiesDropdownComponent'


export default class SearchComponent extends Component {
    constructor() {
        super()
        this.state = {queryData: [], isQueryLoading: false}
        this.queryHandler = this.queryHandler.bind(this)
    }

    async queryHandler(query) {
        this.setState({isQueryLoading: true})
        const res = await get('/query/' + query)
        this.setState({isQueryLoading: false, queryData: res})
    }

    render() {
        return (
            <Container>
                <SearchBarComponent
                    queryHandler={ this.queryHandler }
                />

                <UnversitiesDropdownComponent
                    universities={this.state.queryData.map(obj => obj.uni)}/>
                <br/>

                <Container fluid>
                    <Loader active={this.state.isQueryLoading}></Loader>
                </Container>

                <Dimmer.Dimmable as={Segment} blurring dimmed={this.state.isQueryLoading}>
                    <SearchResultsComponent queryData={this.state.queryData}/>
                </Dimmer.Dimmable>
            </Container>
        )
    }
}
