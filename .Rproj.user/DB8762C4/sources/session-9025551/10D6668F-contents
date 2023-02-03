# This is a script file that we can use to generate figures for our paper


# * Setup -----------------------------------------------------------------

miami_red = '#C3142D'


# * AI Developments -------------------------------------------------------

df = readr::read_csv('recent_developments_ai.csv') |> 
  dplyr::mutate(
    Date = lubridate::mdy(Date),
    Year = lubridate::year(Date),
    Month = lubridate::month(Date)) |> 
  dplyr::arrange(Date) |> 
  dplyr::mutate(position = rep(c(1, -1, 0.5, -0.5),3),
                position2 = rep(c(1.1, -1.1, 0.6, -0.6),3))


df |> 
  ggplot2::ggplot(ggplot2::aes(x = Date, y = 0, label = `AI Method`, col = Company)) + 
  ggplot2::geom_point(ggplot2::aes(y=0), size=1) + 
  ggplot2::geom_hline(yintercept=0, size=0.3) +
  ggplot2::theme_bw(base_size = 8) +
  ggplot2::theme(
    plot.background = ggplot2::element_rect(color = "black"),
    legend.title = ggplot2::element_text(),
    legend.position = 'bottom',
    plot.margin = ggplot2::unit(c(0.1, 0.2, 0.1, 0.1), 'cm'),
    plot.title = ggplot2::element_text(hjust = 0.5, face="bold"),
    plot.subtitle = ggtext::element_markdown(hjust = 0.5, lineheight = 1.5),
    axis.title.y= ggplot2::element_blank(),
    axis.ticks.y= ggplot2::element_blank(),
    # axis.ticks.x = ggplot2::element_blank(),
    axis.text.x= ggplot2::element_text(face = 'bold'),
    axis.title.x= ggplot2::element_text(face = 'bold'),
    axis.text.y= ggplot2::element_blank(),
    panel.grid.major = ggplot2::element_blank(),
    panel.grid.minor = ggplot2::element_blank()
  ) +
  ggplot2::geom_text(ggplot2::aes(y = position2), size = 2.5, fontface = 'bold') +
  ggplot2::geom_segment(ggplot2::aes(y = position, yend=0, xend = Date)) +
  ggplot2::scale_color_brewer(palette = 'Dark2') +
  ggplot2::guides(colour = ggplot2::guide_legend(nrow = 1)) +
  ggplot2::scale_x_date(breaks = scales::pretty_breaks(n=24), limits = c(lubridate::ymd('2020-06-01'), lubridate::ymd('2023-03-15'))) +
  ggplot2::scale_y_continuous(limits = c(-1.25, 1.25)) +
  
  ggplot2::labs(
    caption = expression(paste(bold('Data Source:'),  ' Publicly available release dates of major AI developments.')),
    title = 'A Representative Sample of Major Generative AI Developments from 2020 to Jan 2023')

ggplot2::ggsave(filename = 'figs/ai_dev.pdf', 
                width = 6.5, height = 2)



# * Time to 1 million users -----------------------------------------------

companies = c('ChatGPT', 'Facebook', 'Twitter', 'Instagram',  'Hulu', 'Spotify', 'Pinterest')
time_taken = c(5/30, 10, 24, 2.5, 10, 5, 20)

df_popularity = tibble::tibble(companies, time_taken) |> 
  dplyr::arrange(dplyr::desc(time_taken)) |> 
  dplyr::mutate(companies = forcats::fct_reorder(companies, time_taken))

df_popularity |> 
  ggplot2::ggplot(ggplot2::aes(x = time_taken, y = companies)) +
  ggplot2::geom_bar(stat = 'identity', fill = "white", color = 'black') +
  ggplot2::geom_text(
    mapping = ggplot2::aes(x = time_taken -0.5, y = companies, label = round(time_taken,1)),
    hjust = 1,
    nudge_x = -0.1,
    color = 'black',
    fontface = 'bold',
    size = 2.5
  ) +
  ggplot2::scale_x_continuous(breaks = scales::pretty_breaks(10)) +
  ggplot2::theme_bw(base_size = 8) +
  ggplot2::theme(
    plot.background = ggplot2::element_rect(color = "black"),
    legend.title = ggplot2::element_text(),
    legend.position = 'bottom',
    plot.margin = ggplot2::unit(c(0.1, 0.2, 0.1, 0.1), 'cm'),
    plot.title = ggplot2::element_text(hjust = 0.5, face="bold"),
    plot.subtitle = ggtext::element_markdown(hjust = 0.5),
    axis.title.x= ggplot2::element_text(face="bold"),
    panel.grid.major = ggplot2::element_blank(),
    panel.grid.minor = ggplot2::element_blank()
  ) +
  ggplot2::geom_segment(x = 1.50, xend = 0.1666, y = 1, yend = 1, 
                        arrow =  ggplot2::arrow(length = ggplot2::unit(0.03, "npc")), size = 1) +
  ggplot2::geom_text(
    x = 6, y = 1.25, label = 'It took chatGPT only 5 days \n (0.167 months) to reach 1M users',
    hjust = 0.5,
    color = 'black',
    fontface = 'bold',
    size = 2.5
  ) +
  
  ggplot2::labs(
    x = 'Number of Months to Reach 1 Million Users', y = NULL,
    caption = expression(paste(bold('Data Source:'), ' Business Insider')),
    title = 'Months to Reach 1M Users in Tech'
    # subtitle = "ChatGPT's hype/potential is unprecedented; <br> **5 days** to reach 1M users vs 2+ months for other tech."
  )

ggplot2::ggsave(filename = 'figs/chatGPT.pdf', 
                width = 6.5, height = 2)
