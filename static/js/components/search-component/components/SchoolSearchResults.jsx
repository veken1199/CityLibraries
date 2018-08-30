import React,  { Component }from 'react'
import { Container,  Grid, Segment, Label, Card, Button, Image} from 'semantic-ui-react'

export default class SchoolSearchResults extends Component {
      constructor() {
            super()
            this.state = {}
      }

      render() {
            let data = this.props.data
            let schoolName = this.props.schoolName
            
            return (
                  <Grid.Column>
                        <Label as='a' color='red' ribbon>
                              {schoolName}
                        </Label>

                        {data.map((row, index) => {
                              return ResultCard(row['title'], row['author'], index) 
                              })}
                  </Grid.Column>)
      }
}

const ResultCard = (title:String, author:String, key:int) => (
      <Card raised key = {key} href = "http://google.com">
      <Card.Content>
            <Image floated='right' size='mini' src='http://elektrenumm.lt/wp-content/uploads/2015/03/book_no_cover.jpg' />
            <Card.Header>{ title || "Missing title" }</Card.Header>
            <Card.Meta>Book</Card.Meta>
            <Card.Description>{ author || "Missing author" }</Card.Description>
      </Card.Content>
      <Card.Content extra>
            <div className='ui one buttons'>
            <Button basic color='green'>
                  Checkout 
            </Button>
            </div>
      </Card.Content>
      </Card>
      )