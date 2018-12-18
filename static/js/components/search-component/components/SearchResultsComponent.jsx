import React,  { Component }from 'react'
import { Container,  Grid, Segment, Rail, Sticky, Header, Image, Sidebar } from 'semantic-ui-react'
import SchoolSearchResultsComponent from './SchoolSearchResultsComponent'

export default class SearchResultsComponent extends Component {
      constructor() {
            super()
            this.state = { }      
      }
      

      render() {
            let queryData = this.props.queryData
            return ( 
                  <Container>
                        <Grid columns='3' divided padded celled>
                              <Grid.Row>
                                    {queryData.map((obj, index) => {
                                    return <SchoolSearchResultsComponent 
                                                key = {index} 
                                                schoolName = {obj['uni']}
                                                data = {obj['data']}
                                          />
                                    })}
                              </Grid.Row>
                        </Grid>
                  </Container>
            )
      }
}

