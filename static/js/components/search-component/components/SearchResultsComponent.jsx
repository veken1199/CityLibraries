import React,  { Component }from 'react'
import { Container,  Grid, Segment } from 'semantic-ui-react'
import SchoolSearchResults from './SchoolSearchResults'

export default class SearchResultsComponent extends Component {
      constructor() {
            super()
            this.state = {}
      }

      render() {
            let queryData = this.props.queryData

            return (
                  <Container>
                        <Grid columns='equal'>
                              <Grid.Row>
                                    { queryData.map((row, index) => {
                                    return <SchoolSearchResults 
                                                key = { index } 
                                                schoolName = { row['uni'] }
                                                data = { row['data'] }>
                                          </SchoolSearchResults> 
                                    })}
                              </Grid.Row>
                        </Grid>
                  </Container>
            )
      }
}

