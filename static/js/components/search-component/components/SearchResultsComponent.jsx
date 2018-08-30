import React,  { Component }from 'react'
import { Container,  Grid, Segment } from 'semantic-ui-react'

export default class SearchResultsComponent extends Component {
      constructor() {
            super()
            this.state = {}
      }

      queryUpdateHandler(newQeury) {
            console.log(newQuery);
      }

      render() {
            return (
            <Container>
                  <Grid columns='equal'>
                        <Grid.Row>
                              <Grid.Column>
                                    <Segment>1</Segment>
                              </Grid.Column>
                              <Grid.Column>
                                    <Segment>2</Segment>
                              </Grid.Column>
                        </Grid.Row>
                  </Grid>
            </Container>
            )
      }
}

