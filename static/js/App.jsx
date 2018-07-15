import React, { Component } from 'react'
import { Menu } from 'semantic-ui-react'

export default class MenuExampleHeader extends Component {
  constructor() {
    super()
    this.state = {}
    this.handleItemClick = (e, { name }) => this.setState({ activeItem: name })
  }

  render() {
    const { activeItem } = this.state

    return (
      <Menu color='red'>
        <Menu.Item header>CityLibraries</Menu.Item>
        <Menu.Item
          name='aboutUs'
          active={activeItem === 'aboutUs'}
          onClick={this.handleItemClick}
        />
      </Menu>
    )
  }
}
