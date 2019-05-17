import React, {Component}from 'react'
import {Container, Grid, Segment, Label, Card, Button, Image, Sticky} from 'semantic-ui-react'

export default class SchoolSearchResultsComponent extends Component {
    constructor() {
        super()
        this.state = {}
        this.handleContextRef = contextRef => this.setState({contextRef})
    }

    render() {
        const {contextRef} = this.state
        let data = this.props.data
        let schoolName = this.props.schoolName

        return (
            <Grid.Column>
                <Label as='a' color='red' ribbon id={schoolName}>
                    {schoolName}
                </Label>

                <Container style={{overflowY: 'scroll', maxHeight: Math.round(window.innerWidth * 0.3)}}
                           ref={this.handleContextRef}>
                    {data.map((row, index) => {
                        return ResultCard(row['title'], row['author'], index)
                    })}
                </Container>
            </Grid.Column>
        )
    }
}

const ResultCard = (title, author, key) => (
    <Card raised key={key} href="http://google.com">
        <Card.Content>
            <Image floated='right' size='mini'
                   src='http://elektrenumm.lt/wp-content/uploads/2015/03/book_no_cover.jpg'/>
            <Card.Header>{title || "Missing title"}</Card.Header>
            <Card.Meta>Book</Card.Meta>
            <Card.Description>{author || "Missing author"}</Card.Description>
        </Card.Content>
    </Card>
)