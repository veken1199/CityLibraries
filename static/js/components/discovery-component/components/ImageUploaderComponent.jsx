import {Button, Input, Container, TextArea, Form, Modal, Header, Icon, Image, Loader} from 'semantic-ui-react'
import React, {useState} from 'react'
import {uploadImage} from '../../../helpers/request-handler'


export class ImageUploader extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            imageToBeSent: "",
            imageTitle: "",
            imageDescription: "",
            isUploading: false
        }
    }

    async initImageUploading() {
        const {imageToBeSent, imageTitle, imageDescription} = this.state
        if (!imageToBeSent) {
            alert("Ah! You forgot to choose a picture")
        }
        if(imageToBeSent.size > 4 * 1024 * 1024){
            alert("Wow the picture is too big")
        }
        else if (!imageTitle) {
            alert("Ah! You forgot to write the title of the book")
        } else {
            this.setState({isUploading: true})
            const res = await uploadImage(imageToBeSent, imageTitle, imageDescription);
            res.message && alert(res.message)
            this.setState({isUploading: false})
            if (res.hasOwnProperty("has_error")&& res.has_error === false) {
                window.location.reload();
            }
        }
    }

    render() {
        return (
            <Container textAlign={"left"} style={{ margin: "20", width: "80%", float: "left"}}>
                <p>Upload a picture of the book and we will show if for a week!</p>
                <Modal trigger={<Button color="green">Let's go!</Button>} closeIcon>
                    <Header icon='archive' content='Share with us what you are reading '/>
                    <Modal.Content>
                        <Image wrapped size='medium' src={this.state.imageToBeSent.path}/>
                        <Form>
                            <Form.Group widths='equal'>
                                <Form.Field control={Input}
                                            required
                                            minLength="1"
                                            maxLength="100"
                                            label='Title (100 characters max)'
                                            placeholder='Title'
                                            onChange={e => this.setState({imageTitle: e.target.value})}/>
                            </Form.Group>
                            <Form.Field control={TextArea}
                                        label='Tell us more about it (200 characters max)'
                                        maxLength="200"
                                        placeholder='Tell us more about the book...'
                                        onChange={e => this.setState({imageDescription: e.target.value})}/>
                            <Form.Field control={Input} type={"file"} label={"Book's picture (max 4M)"}
                                        onChange={e => this.setState({imageToBeSent: e.target.files[0]})}/>
                        </Form>
                    </Modal.Content>
                    <Modal.Actions>
                        <Loader float={"left"} active={this.state.isUploading} inline />
                        <Button color='green' loading={this.state.isUploading}
                                onClick={this.initImageUploading.bind(this)}>
                            <Icon name='cloud'/> Ship it
                        </Button>
                    </Modal.Actions>
                </Modal>
            </Container>
        )
    }
}
