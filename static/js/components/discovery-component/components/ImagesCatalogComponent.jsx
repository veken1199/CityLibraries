import React from 'react'
import {Grid, Image, Card} from 'semantic-ui-react'

export class ImagesCatalogComponent extends React.Component {
    constructor(props) {
        super(props)
    }

    render() {
        const booksData = this.props.booksData
        return (
            <Grid divided='vertically'>
                <Grid.Row columns={3} style={{overflowX: 'scroll'}}>
                    {booksData.map((booksData, index) =>
                        (
                            <Grid.Column key={index}>
                                {createImageCardForBook(booksData)}
                            </Grid.Column>
                        )
                    )}
                </Grid.Row>
            </Grid>
        )
    }
}

const createImageCardForBook = (bookData) => (
    <Card>
        <Image src={bookData.image_url} wrapped ui={false}/>
        <Card.Content>
            <Card.Header>{bookData.title}</Card.Header>
            <Card.Meta>
                <span className='date'>{bookData.posted_on}</span>
            </Card.Meta>
            <Card.Description>
                {bookData.description}
            </Card.Description>
        </Card.Content>
    </Card>
)

