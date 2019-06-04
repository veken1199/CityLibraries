import React from 'react'
import {ImageUploader} from './components/ImageUploaderComponent'
import {ImagesCatalogComponent} from './components/ImagesCatalogComponent'
import {Container, Message, Divider, Pagination} from 'semantic-ui-react'
import {get} from '../../helpers/request-handler'


export class DiscoveryComponent extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            books: [],
            totalPageNums: 0
        }
    }

    componentDidMount() {
        this.getBooks(null, {activePage: 1})
    }

    async getBooks(e, {activePage}) {
        const res = await get(`/image/${activePage}`)
        res.data && this.setState({books: res.data, totalPageNums: res.total_page_nums})
    }

    render() {
        return (
            <Container>
                <Message
                    icon='cloud'
                    header='Wanna tell us what you are reading this week?'
                    content={<ImageUploader />}
                >
                </Message>

                <Divider/>
                <ImagesCatalogComponent booksData={this.state.books}/>
                <Divider/>

                <Container>
                    <Pagination float="center"
                                defaultActivePage={1}
                                firstItem={null}
                                lastItem={null}
                                pointing
                                secondary
                                totalPages={this.state.totalPageNums}
                                onPageChange={this.getBooks.bind(this)}
                    />
                </Container>
            </Container>

        )
    }
}