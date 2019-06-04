import React, {Component}from 'react'
import {Container, Grid, Segment, Rail, Sticky, Header, Image, Sidebar} from 'semantic-ui-react'
import SchoolSearchResultsComponent from './SchoolSearchResultsComponent'

const maxNumOfColumns = 3 ;
export default class SearchResultsComponent extends Component {
    constructor() {
        super()
    }

    render() {
        let queryRespData = this.props.queryRespData
        let numberOfColumnsInData = queryRespData.length === 0 ? maxNumOfColumns : queryRespData.length
        return (
            <Container>
                <Grid columns={Math.min(numberOfColumnsInData , maxNumOfColumns)} divided padded celled>
                    <Grid.Row>
                        {queryRespData.map((obj, index) => (
                            <SchoolSearchResultsComponent
                                key={index}
                                schoolName={obj.university_name}
                                data={obj.library_result_items}
                            />
                        ))}
                    </Grid.Row>
                </Grid>
            </Container>
        )
    }
}

