import { QuartzComponentConstructor, QuartzComponentProps } from "./types"

export default (() => {
  function PeopleGrid({ allFiles, fileData }: QuartzComponentProps) {
    const currentSlug = fileData.slug ?? ""
    if (!currentSlug.startsWith("wiki/people/index")) return null

    const people = allFiles
      .filter((f) => {
        const slug = f.slug ?? ""
        return slug.startsWith("wiki/people/") && slug !== "wiki/people/index" && !slug.endsWith("/README")
      })
      .sort((a, b) => {
        const nameA = (a.frontmatter?.title as string) ?? a.slug ?? ""
        const nameB = (b.frontmatter?.title as string) ?? b.slug ?? ""
        return nameA.localeCompare(nameB)
      })

    if (people.length === 0) return null

    return (
      <div class="people-grid">
        {people.map((person) => {
          const name = (person.frontmatter?.title as string) ?? person.slug ?? "Unknown"
          const role = person.frontmatter?.role as string | undefined
          const org = person.frontmatter?.org as string | undefined
          const slug = person.slug ?? ""
          const initials = name
            .split(" ")
            .map((w: string) => w[0])
            .join("")
            .toUpperCase()
            .slice(0, 2)

          return (
            <a href={`/${slug}`} class="person-card">
              <div class="person-avatar">{initials}</div>
              <div class="person-info">
                <div class="person-name">{name}</div>
                {role && <div class="person-role">{role}</div>}
                {org && <div class="person-org">{org}</div>}
              </div>
            </a>
          )
        })}
      </div>
    )
  }

  PeopleGrid.css = `
    .people-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(180px, 1fr));
      gap: 12px;
      margin: 1.5rem 0;
    }
    .person-card {
      display: flex;
      align-items: center;
      gap: 10px;
      padding: 10px 12px;
      border-radius: 8px;
      border: 1px solid var(--lightgray);
      text-decoration: none;
      color: var(--dark);
      transition: background 0.15s, border-color 0.15s;
    }
    .person-card:hover {
      background: var(--light);
      border-color: var(--gray);
    }
    .person-avatar {
      width: 36px;
      height: 36px;
      border-radius: 50%;
      background: var(--secondary);
      color: var(--light);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 0.75rem;
      font-weight: 600;
      flex-shrink: 0;
    }
    .person-info {
      overflow: hidden;
    }
    .person-name {
      font-size: 0.85rem;
      font-weight: 600;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }
    .person-role {
      font-size: 0.7rem;
      color: var(--gray);
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }
    .person-org {
      font-size: 0.7rem;
      color: var(--gray);
      opacity: 0.7;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }
  `

  return PeopleGrid
}) satisfies QuartzComponentConstructor
