import React, {Component} from "react";
import {Container, Grid, Label, Card, Image} from "semantic-ui-react";

export default class SchoolSearchResultsComponent extends Component {
    constructor() {
        super()
        this.state = {}
    }

    render() {
        let data = this.props.data
        let schoolName = this.props.schoolName

        return (
            <Grid.Column>
                <Label as='a' color='red' ribbon id={schoolName}>
                    {schoolName}
                </Label>

                <Container style={{overflowY: 'scroll', maxHeight: Math.round(window.innerWidth * 0.3)}}>
                    {data.map((row, index) => {
                        return ResultCard(row, index)
                    })}
                </Container>
            </Grid.Column>
        )
    }
}

const ResultCard = (row, key) => (
    <Card raised key={key} href={row.link} target={"_blank"}>
        <Card.Content>
            { row.link &&
            <Image floated='right' size='mini'
                   src='https://cdn4.iconfinder.com/data/icons/internet-seo-and-online-activity/400/Internet_online_world_wide_web_globe_network-512.png'/>
            }
            <Card.Header>{row.title || "Missing title"}</Card.Header>
            <Card.Meta>Book</Card.Meta>
            <Card.Description>{row.author || "Missing author"}</Card.Description>
        </Card.Content>
    </Card>
)