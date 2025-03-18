# GrubText Encyclopedia

GrubText is a powerful, command-line-based encyclopedia management system designed for users who need a robust and flexible way to create, edit, search, export, import, and manage pages of information. Built with Python and leveraging the `rich` library for a visually appealing interface, GrubText provides an intuitive and efficient way to handle large volumes of textual data. Whether you're managing personal notes, a knowledge base, or a collaborative project, GrubText offers the tools you need to stay organized and productive.

## Features

- **View Pages**: Browse through all available pages in your encyclopedia with ease.
- **Create New Page**: Quickly create new pages with customizable titles, content, and metadata.
- **Edit Page**: Modify existing pages to keep your information up-to-date.
- **Search Pages**: Perform keyword searches across all pages to find relevant information instantly.
- **Export Page**: Share your pages by exporting them to a shared directory.
- **Import Page**: Import pages from the shared directory to incorporate external content.
- **Backup & Restore**: Safeguard your data with automated backups and restore functionality.
- **User-Friendly Interface**: A clean, visually rich interface powered by the `rich` library ensures a seamless user experience.

## Installation

To get started with GrubText, follow these simple steps:

1. **Download the Script**:
   Use `wget` to download the latest version of GrubText directly from the repository:
   ```bash
   wget https://raw.githubusercontent.com/linuxfanboy4/GrubText/refs/heads/main/src/gruptext.py
   ```

2. **Run the Script**:
   Execute the script using Python 3:
   ```bash
   python3 gruptext.py
   ```

3. **Start Using GrubText**:
   Once the script is running, you will be presented with the main menu. From here, you can explore all the features GrubText has to offer.

## Usage

### Main Menu
Upon launching GrubText, you will be greeted with the main menu, which provides access to all the core functionalities:

1. **View Pages**: Displays a list of all available pages. Select a page to view its content.
2. **Create New Page**: Create a new page by providing a title, content, and optional author information.
3. **Edit Page**: Edit the content of an existing page.
4. **Search Pages**: Search for pages containing specific keywords.
5. **Export Page**: Export a page to the shared directory for easy sharing.
6. **Import Page**: Import a page from the shared directory into your local encyclopedia.
7. **Backup & Restore**: Create a backup of your entire encyclopedia or restore from an existing backup.
8. **Exit**: Exit the application.

### Creating a New Page
To create a new page, select the "Create New Page" option from the main menu. You will be prompted to enter a title, content, and an optional author name. The page will be saved in the `grubtext_pages` directory with a `.grup` extension.

### Editing a Page
To edit an existing page, choose the "Edit Page" option from the main menu. Select the page you wish to edit, and you will be prompted to enter new content. The updated page will be saved automatically.

### Searching Pages
The "Search Pages" feature allows you to search for pages containing specific keywords. Simply enter your search query, and GrubText will display a list of matching pages. You can then view any of the matched pages directly from the search results.

### Exporting and Importing Pages
GrubText makes it easy to share pages with others. Use the "Export Page" option to copy a page to the `shared_grubtext` directory. Conversely, use the "Import Page" option to bring pages from the shared directory into your local encyclopedia.

### Backup and Restore
GrubText includes a robust backup and restore system. You can create a backup of your entire encyclopedia with a single command, ensuring that your data is safe. If needed, you can restore your encyclopedia from any available backup.

## Directory Structure

- **grubtext_pages**: This directory contains all your local pages. Each page is stored as a `.grup` file, which includes both the content and metadata.
- **shared_grubtext**: This directory is used for exporting and importing pages. Pages placed here can be easily shared with other users.
- **backup_YYYYMMDDHHMMSS**: Backup directories are automatically created with a timestamp, allowing you to restore your encyclopedia to a specific point in time.

## Dependencies

GrubText relies on the following Python libraries:

- **rich**: A library for rich text and beautiful formatting in the terminal. Install it using:
  ```bash
  pip install rich
  ```

## Contributing

Contributions to GrubText are welcome! If you have ideas for new features, improvements, or bug fixes, please feel free to submit a pull request or open an issue on the GitHub repository.

## License

GrubText is released under the MIT License. See the LICENSE file for more details.

## Support

For any questions, issues, or feedback, please visit the [GitHub repository](https://github.com/linuxfanboy4/GrubText) or contact the maintainers directly.

---

GrubText is designed to be a powerful, yet simple tool for managing textual information. Whether you're a developer, researcher, or just someone who loves to organize knowledge, GrubText is here to make your life easier. Start using it today and experience the future of encyclopedia management!
